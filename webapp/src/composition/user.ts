import { Store } from "@/core/store";
import request from "@/core/api";
import { Role } from "@/composition/role";
import { reactive } from "vue";

// MODEL

interface User {
  username: string;
  email: string;
  roles: Role[];
}

// USER STORE

interface UserStoreState {
  user: User | null;
  authenticated: boolean;
}

class UserStore extends Store<UserStoreState> {
  protected data(): UserStoreState {
    return { user: null, authenticated: false };
  }
}

const userStore = new UserStore();

// USER METHODS

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

const logout = async (): Promise<void> => {
  await request.post("/user/logout", {});
  userStore.setState({ user: null, authenticated: false });
};

const hasRole = (role: string): boolean => {
  const _hasRole = (_user: User, _role: string) =>
    _user.roles.filter((r) => r.name === _role).length > 0;
  const user = userStore.state.user;
  if (!user) return false;
  if (_hasRole(user, "root")) return true;
  return _hasRole(user, role);
};

// USE USER

interface UseUserParams {
  login: (username: string, password: string) => Promise<void>;
  logout: () => Promise<void>;
  hasRole: (role: string) => boolean;
  fetchUserInfo: () => Promise<void>;
}

const useUser = (): UseUserParams => {
  return {
    login,
    logout,
    hasRole,
    fetchUserInfo,
  };
};

// USERS METHODS

const getUsers = async (): Promise<User[]> => {
  const res = await request.get<User[]>("/user");
  return res.data;
};

// USE USERS

interface UsersState {
  users: User[];
}

interface UseUsersParams {
  state: UsersState;
  getUsers: () => Promise<User[]>;
}

const useUsers = (): UseUsersParams => {
  return {
    state: reactive({ users: [] }),
    getUsers,
  };
};

// EXPORT

export { User, userStore, useUser, useUsers };
