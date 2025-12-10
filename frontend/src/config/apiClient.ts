import axios from "axios";

const options = {
  baseURL: import.meta.env.VITE_API_URL,
  withCredentials: true
}

const API = axios.create(options)

// frontend/src/config/apiClient.ts
API.interceptors.response.use(
  res => res,
  err => {
    const { config, response } = err;
    if (response && config?.url?.includes("/user") && [404, 422].includes(response.status)) {
      localStorage.removeItem("user_id");
      window.location.reload(); // forces refresh
    }
    return Promise.reject(err);
  }
);



export default API
