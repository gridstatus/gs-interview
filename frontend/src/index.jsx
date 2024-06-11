import React from "react";
import ReactDOM from "react-dom/client";

import "react-grid-layout/css/styles.css";
import "react-resizable/css/styles.css";

import "@mantine/core/styles.css";
import "@mantine/dates/styles.css";
import "@mantine/notifications/styles.css";

import App from "./App";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);
