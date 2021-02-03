import ApiRequest from "@/core/api";
import { HttpMethod } from "@/core/requests";
import User from "@/composition/user/model";
import userStore from "@/composition/user/store";

const getUserInfo = async (): Promise<void> => {
  userStore.setState({ loading: true });
  try {
    const request = new ApiRequest(HttpMethod.get, "/user/info");
    const response = await request.fetch<User>();
    userStore.setState({ user: response.data, loading: false });
  } catch (e) {
    userStore.setState({ user: undefined, loading: false });
  }
};

const login = async (username: string, password: string): Promise<void> => {
  const request = new ApiRequest(HttpMethod.post, "/user/login", {
    username: username,
    password: password,
  });
  const response = await request.fetch<User>();
  userStore.setState({ user: response.data });
};

const logout = async (): Promise<void> => {
  const request = new ApiRequest(HttpMethod.post, "/user/logout");
  await request.fetch();
  userStore.setState({ user: undefined });
};

export { getUserInfo, login, logout };
