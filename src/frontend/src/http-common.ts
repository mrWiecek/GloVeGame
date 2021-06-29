import axios, { AxiosInstance } from "axios";

const apiClient: AxiosInstance = axios.create({
  // baseURL: "http://localhost:8080/api/",
  baseURL: "https://jsonplaceholder.typicode.com/",
  headers: {
    "Content-type": "application/json",
  },
});

export default apiClient;
