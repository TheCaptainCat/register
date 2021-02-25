import { Store } from "@/core/store";
import request from "@/core/api";
import { Role } from "@/composition/role";

interface User {
  username: string;
  email: string;
  roles: Role[];
}

interface UserState {
  user: User | null;
  authenticated: boolean;
}

class UserStore extends Store<UserState> {
  protected data(): UserState {
    return { user: null, authenticated: false };
  }
}

const userStore = new UserStore();

const fetchUserInfo = async (): Promise<void> => {
  const res = await request.get<User>("/user/info");
  userStore.setState({ user: res.data, authenticated: true });
};

const login = async (username: string, password: string): Promise<void> => {
  const res = await request.post<object, User>("/user/login", {
    username,
    password,
  });
  userStore.setState({ user: res.data, authenticated: true });
};

export { User, userStore, fetchUserInfo, login };
