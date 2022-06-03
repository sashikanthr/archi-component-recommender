import xml.etree.ElementTree as ET
import os


class ArchiComponent:

    def __init__(self, component_type, component_name, component_id, model_id, model_name):
        self.model_id = model_id
        self.component_type = component_type
        self.component_name = component_name
        self.component_id = component_id
        self.model_name = model_name

    def get_model_id(self):
        return self.model_id

    def get_component_type(self):
        return self.component_type

    def get_component_name(self):
        return self.component_name

    def get_component_id(self):
        return self.component_id

    def get_model_name(self):
        return self.model_name


def parse_archi_xml():
    archi_components = []
    # Archi models are picked up from -
    # https://github.com/borkdominik/CM2KG/tree/main/Experiments/EMF/Archi/ManyModels/repo-github-archimate/models
    path = 'D://github//archi_models'

    for archi_xml in os.listdir(path):
        file_name = path + "//" + archi_xml
        tree = ET.parse(file_name)
        print(f'Processing....,{file_name}')
        root = tree.getroot()
        model_id = root.attrib['identifier']
        xmlns = root.tag.replace('model', '')
        schema = 'schemaLocation'
        location = ''
        for key in root.keys():
            if schema in key:
                location = key.replace(schema, '')
                break
        model_name = root.find(xmlns + 'name').text
        next_root = root.find(xmlns + 'elements')
        if next_root is not None:
            for child in root.find(xmlns + 'elements'):
                component_id = child.attrib['identifier']
                name = child.find(xmlns + 'name').text
                component_type = child.attrib[location + 'type']
                archi_component = ArchiComponent(component_type, name, component_id, model_id, model_name)
                archi_components.append(archi_component)

    return group_by_type(archi_components)


def group_by_type(archi_components):
    components_by_type = {}
    a = 0
    for component in archi_components:
        a = a + 1
        component_type = component.get_component_type()
        values = []
        if component_type in components_by_type:
            value = components_by_type[component_type]
            value.append(component)

        else:
            values.append(component)
            components_by_type[component_type] = values
    return components_by_type
