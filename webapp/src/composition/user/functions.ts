import ApiRequest from "@/core/api";
import { HttpMethod } from "@/core/requests";
import User from "@/composition/user/model";
import userStore from "@/composition/user/store";

async function getUserInfo() {
  userStore.setState({ loading: true });
  try {
    const request = new ApiRequest(HttpMethod.get, "/user/info");
    const response = await request.fetch<User>();
    userStore.setState({ user: response.data, loading: false });
  } catch (e) {
    userStore.setState({ user: undefined, loading: false });
  }
}

async function login(username: string, password: string) {
  const request = new ApiRequest(HttpMethod.post, "/user/login", {
    username: username,
    password: password
  });
  const response = await request.fetch<User>();
  userStore.setState({ user: response.data });
}

async function logout() {
  const request = new ApiRequest(HttpMethod.post, "/user/logout");
  await request.fetch();
  userStore.setState({ user: undefined });
}

export default function useUser() {
  return {
    getUserInfo,
    login,
    logout
  };
}
