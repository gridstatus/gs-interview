import React, { useState } from "react";
import { Select, Table, Loader, Container, Text, Stack } from "@mantine/core";
import useData from "../hooks/useData";
import useTables from "../hooks/useTables";

const DataTable = () => {
  const [tableName, setTableName] = useState("");
  const {
    data: tables,
    error: tablesError,
    isLoading: isLoadingTables,
  } = useTables();

  const { data, error, isLoading } = useData({
    tableName,
    limit: 10,
    enabled: tableName !== "",
  });

  const handleTableChange = (value) => {
    setTableName(value);
  };

  return (
    <Container>
      <Stack>
        <Text size="xl" weight={700} align="center" mt="xl" mb="md">
          Data Table
        </Text>
        {isLoadingTables ? (
          <Loader size="lg" />
        ) : tablesError ? (
          <Text c="red" align="center">
            Error loading tables: {tablesError.message}
          </Text>
        ) : (
          <Select
            placeholder="Select a table"
            value={tableName}
            onChange={handleTableChange}
            data={tables.map((table) => ({ value: table, label: table }))}
          />
        )}

        {isLoading ? (
          <Loader size="lg" />
        ) : error ? (
          <Text c="red" align="center">
            Error: {error.message}
          </Text>
        ) : (
          tableName && (
            <Table striped highlightOnHover withColumnBorders>
              <Table.Thead>
                <Table.Tr>
                  {data?.length > 0 &&
                    Object.keys(data[0]).map((key) => <th key={key}>{key}</th>)}
                </Table.Tr>
              </Table.Thead>
              <Table.Tbody>
                {data?.map((item, index) => (
                  <Table.Tr key={index}>
                    {Object.values(item).map((value, i) => (
                      <td key={i}>{value}</td>
                    ))}
                  </Table.Tr>
                ))}
              </Table.Tbody>
            </Table>
          )
        )}
      </Stack>
    </Container>
  );
};

export default DataTable;
