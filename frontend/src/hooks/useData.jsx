import { useQuery } from "@tanstack/react-query";
import axios from "axios";

const useData = (tableName, limit = 25) => {
  const fetchData = async () => {
    const response = await axios.get(`${import.meta.env.VITE_API_HOST}/data`, {
      params: { table_name: tableName, limit },
    });
    return response.data;
  };

  return useQuery(["data", tableName, limit], fetchData);
};

export default useData;
