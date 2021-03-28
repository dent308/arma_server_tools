import os
import yaml


class Generator(object):
    def __init__(self):
        self.field_meta = self.parse_field_names()

    def parse_field_names(self):
        result = None
        this_dir, this_filename = os.path.split(__file__)
        fields_file = os.path.join(this_dir, "server_field_names.yaml")
        with open(fields_file) as stream:
            try:
                result = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        return result

    # hostname = "Fun and Test Server";
    # motdInterval = 5;
    def simple_item(self, key, value):

        if isinstance(value, int) or isinstance(value, float):
            return f'{key} = {value};'
        else:
            return f'{key} = "{value}";'

    # missionWhitelist[] = {
    #   "direct_action_dev.Altis",
    # };
    # list_items('missionWhiteList', 'direct_action_dev.Altis', true, false)
    def list_items(self, key, values, newlines=True):

        product = []
        if newlines:
            newline = "\n"
        else:
            newline = ""
    
        product.append(f"{key}[] = {{{newline}")
        for item in values:
            if isinstance(item, str):
                quote = '"'
            product.append(f"  {quote}{item}{quote},{newline}")
        product.append(f"}};{newline}")

        return "".join(product)

    def nested_list_items(self, key, values, newlines=True):
        product = []
        if newlines:
            newline = ""
        else:
            newline = '\n'
        product.append(f"{key}[] = {{{newline}")
        for line in values:
            line_items = ""
            product.append(f'{{')
            for item in line:
                if isinstance(item, str):
                    line_items += f'"{item}", '
                elif isinstance(item, bool):
                    if item:
                        line_items += f'true, '
                    else:
                        line_items += f'false, '
                elif isinstance(item, int) or isinstance(item, float):
                    line_items += str(item)
                else:
                    line_items.append(item)

            product.append(f"  {line_items} }},{newline}")

        product.append(f"}};{newline}")
        return "".join(product)


    def generate(self, server_yaml_file):
        data = None
        product = []
        with open(server_yaml_file) as stream:
            try:
                data = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

        for key in data:
            value = data[key]
            # print(f'{key} : {value}')
            if key in self.field_meta['lists']:
                self.produce_list(key, value, product)

            elif key in self.field_meta['nested_lists']:
                self.produce_nested_list(key, value, product)

            elif key in self.field_meta['specials']:
                self.produce_special(key, value, product)

            elif key in self.field_meta['reserved']:
                print(f"RESERVED: {key}")

            else:
                self.produce_simple(key, value, product)

        return("\n".join(product))

    def produce_simple(self, key, value, product):
        product.append(self.simple_item(key, value))

    def produce_list(self, key, value, product):
        if isinstance(value, list):
            product.append(self.list_items(key, value))

    def produce_nested_list(self, key, value, product):
         product.append(self.nested_list_items(key, value))


    def produce_special(self, key, value, product):
        # product.append(value)
        pass
