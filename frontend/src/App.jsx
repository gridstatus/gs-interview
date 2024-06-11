import React from "react";
import DataTable from './components/DataTable';

const App = () => {
  return (
    <div>
      <h1>Hello World</h1>
      <DataTable tableName="caiso_fuel_mix" limit={10} />
    </div>
  );
};

export default App;
