import ArchiXMLParser
import SimilarityModel


def get_component_names_by_type(component_type: str, component_map: dict):
    if component_type in component_map:
        component_map = component_map[component_type]
        return list(map(lambda c: [c.get_component_name()], component_map))


if __name__ == '__main__':
    archi_components = ArchiXMLParser.parse_archi_xml()
    component_names = get_component_names_by_type("BusinessObject", archi_components)
    print(f'Number of unique names >> {len(component_names)}')
    print(component_names)
    SimilarityModel.word_2_vec(component_names)

