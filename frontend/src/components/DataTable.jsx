import React, { useState } from "react";
import { Select, Table, Loader, Container, Text } from "@mantine/core";
import useData from "../hooks/useData";
import useTables from "../hooks/useTables";

const DataTable = () => {
  const [tableName, setTableName] = useState("");
  const {
    data: tables,
    error: tablesError,
    isLoading: isLoadingTables,
  } = useTables();
  const { data, error, isLoading } = useData(tableName, 10);

  const handleTableChange = (value) => {
    setTableName(value);
  };

  return (
    <Container>
      <Text size="xl" weight={700} align="center" mt="xl" mb="md">
        Data Table
      </Text>
      {isLoadingTables ? (
        <Loader size="lg" />
      ) : tablesError ? (
        <Text color="red" align="center">
          Error loading tables: {tablesError.message}
        </Text>
      ) : (
        <Select
          placeholder="Select a table"
          value={tableName}
          onChange={handleTableChange}
          data={tables.map((table) => ({ value: table, label: table }))}
          mb="md"
          styles={{ input: { textAlign: "center" } }}
        />
      )}

      {isLoading ? (
        <Loader size="lg" />
      ) : error ? (
        <Text color="red" align="center">
          Error: {error.message}
        </Text>
      ) : (
        tableName && (
          <Table striped highlightOnHover withBorder withColumnBorders>
            <thead>
              <tr>
                {data?.length > 0 &&
                  Object.keys(data[0]).map((key) => <th key={key}>{key}</th>)}
              </tr>
            </thead>
            <tbody>
              {data?.map((item, index) => (
                <tr key={index}>
                  {Object.values(item).map((value, i) => (
                    <td key={i}>{value}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </Table>
        )
      )}
    </Container>
  );
};

export default DataTable;
