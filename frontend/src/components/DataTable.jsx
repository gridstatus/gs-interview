import React from "react";
import { useQuery } from "@tanstack/react-query";
import axios from "axios";
import { Table, Loader, Alert } from "@mantine/core";

const fetchTableData = async ({ queryKey }) => {
  const [_, tableName, limit] = queryKey;
  const { data } = await axios.get(`/data?$table_name=${tableName}`, {
    params: {
      tableName,
      limit,
    },
  });
  return data;
};

const DataTable = ({ tableName, limit }) => {
  const { data, error, isLoading } = useQuery({
    queryKey: ["tableData", tableName, limit],
    queryFn: fetchTableData,
    enabled: !!tableName,
  });

  console.log(data);

  if (isLoading || !data) {
    return <Loader />;
  }

  if (error) {
    return (
      <Alert title="Error" color="red">
        {error.message}
      </Alert>
    );
  }

  return (
    <Table>
      <thead>
        <tr>
          {data.length > 0 &&
            Object.keys(data[0]).map((key) => <th key={key}>{key}</th>)}
        </tr>
      </thead>
      <tbody>
        {data.length > 0 &&
          data.map((row, index) => (
            <tr key={index}>
              {Object.values(row).map((value, i) => (
                <td key={i}>{value}</td>
              ))}
            </tr>
          ))}
      </tbody>
    </Table>
  );
};

export default DataTable;
