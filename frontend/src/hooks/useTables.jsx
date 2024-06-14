import { useQuery } from "@tanstack/react-query";
import axios from "axios";

const fetchTables = async () => {
  const response = await axios.get(`${import.meta.env.VITE_API_HOST}/tables`);
  return response.data.tables;
};

const useTables = () => {
  return useQuery({
    queryKey: ["tables"],
    queryFn: fetchTables,
  });
};

export default useTables;
