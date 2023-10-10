import { DataNode } from "antd/es/tree";
import { OilfieldType, OperationalUnitType, WellType } from "../@types/domain";

/**
 * Função que processa os dados para o formato solicitado
 */

export function processData(
  opunits: OperationalUnitType[],
  oilfields: OilfieldType[],
  wells: WellType[]
): DataNode[] {
  const tree: DataNode[] = [];

  for (const opunit of opunits) {
    const opunitNode: DataNode = {
      title: opunit.name,
      key: `opunit-${opunit.id}`,
      children: [],
    };

    const associatedOilfields = oilfields.filter(
      (oilfield) => oilfield.operational_unit === opunit.id
    );

    for (const oilfield of associatedOilfields) {
      const oilfieldNode: DataNode = {
        title: oilfield.name,
        key: `oilfield-${oilfield.id}`,
        children: [],
      };

      const associatedWells = wells.filter(
        (well) => well.oilfield === oilfield.id
      );

      for (const well of associatedWells) {
        const wellNode: DataNode = {
          title: well.name,
          key: `well-${well.id}`,
        };


        if (oilfieldNode.children)
          oilfieldNode.children.push(wellNode);
      }

      if (opunitNode.children)
        opunitNode.children.push(oilfieldNode);
    }

    tree.push(opunitNode);
  }

  return tree;
}