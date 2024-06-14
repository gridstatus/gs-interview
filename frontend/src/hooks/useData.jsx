import { useQuery } from "@tanstack/react-query";
import axios from "axios";

const fetchData = async ({ queryKey }) => {
  const [_key, { tableName, limit }] = queryKey;
  const response = await axios.get(`${import.meta.env.VITE_API_HOST}/data`, {
    params: { table_name: tableName, limit },
  });
  return response.data;
};

const useData = (tableName, limit) => {
  return useQuery({
    queryKey: ["data", { tableName, limit }],
    queryFn: fetchData,
  });
};

export default useData;
