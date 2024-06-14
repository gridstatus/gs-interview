import { useQuery } from "@tanstack/react-query";
import axios from "axios";

const fetchData = async ({ tableName, limit }) => {
  const response = await axios.get(`${import.meta.env.VITE_API_HOST}/data`, {
    params: { table_name: tableName, limit },
  });
  return response.data;
};

const useData = ({ tableName, limit, enabled = true }) => {
  return useQuery({
    queryKey: ["data", { tableName, limit }],
    queryFn: () => fetchData({ tableName, limit }),
    enabled,
  });
};

export default useData;
