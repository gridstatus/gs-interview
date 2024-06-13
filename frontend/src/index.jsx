import React from "react";
import ReactDOM from "react-dom/client";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { MantineProvider } from "@mantine/core";

import "react-grid-layout/css/styles.css";
import "react-resizable/css/styles.css";

import "@mantine/core/styles.css";
import "@mantine/dates/styles.css";
import "@mantine/notifications/styles.css";

import App from "./App";

const queryClient = new QueryClient();

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <MantineProvider>
      <QueryClientProvider client={queryClient}>
        <App />
      </QueryClientProvider>
    </MantineProvider>
  </React.StrictMode>,
);
