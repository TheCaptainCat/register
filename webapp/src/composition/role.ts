// MODEL

import request from "@/core/api";
import { User } from "@/composition/user";

interface Role {
  name: string;
}

// ROLES METHODS

const getRoles = async (): Promise<Role[]> => {
  const res = await request.get<Role[]>("/role");
  return res.data;
};

const addRoleToUser = async (role: Role, user: User): Promise<User> => {
  const res = await request.post<Role, User>(
    `/user/${user.username}/roles`,
    role
  );
  return res.data;
};

// USE ROLES

interface RolesState {
  roles: Role[];
}

interface UseRolesParams {
  state: RolesState;
  getRoles: () => Promise<Role[]>;
  addRoleToUser: (role: Role, user: User) => Promise<User>;
}

const useRoles = (): UseRolesParams => {
  return {
    state: { roles: [] },
    getRoles,
    addRoleToUser,
  };
};

export { Role, useRoles };
