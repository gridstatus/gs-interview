import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";

export default defineConfig(() => {
  return {
    server: {
      open: true,
      port: 3000,
    },
    build: {
      outDir: "build",
      sourcemap: true,
    },
    base: "/",
    plugins: [react()],
  };
});
