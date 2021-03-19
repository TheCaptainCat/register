<template>
  <loading v-if="state.loading" />
  <div v-else class="admin-users">
    <h1 class="table-title">
      {{ i18n.t("views.admin.users.title") }}
    </h1>
    <data-table :columns="tableColumns" :items="usersState.users">
      <template v-slot:body="{ items }">
        <tr
          v-for="user in items"
          :key="user.username"
          class="user-line"
          @click="clickUserLine(user)"
        >
          <td>{{ user.username }}</td>
          <td>{{ user.email }}</td>
          <td>
            <span v-for="role in user.roles" :key="role.name" class="role-tag">
              {{ role.name }}
            </span>
          </td>
        </tr>
      </template>
    </data-table>
    <template v-if="state.selectedUser !== null">
      <h1 class="user-details-title">
        {{ state.selectedUser.username }}
        <span>{{ state.selectedUser.email }}</span>
      </h1>
      <div class="user-roles flex aic" v-if="state.selectedUser.roles">
        <h4>{{ i18n.t("views.admin.users.columns.roles") }}</h4>
        <span
          v-for="role in state.selectedUser.roles"
          :key="role.name"
          class="role-tag with-icon"
        >
          <span>{{ role.name }}</span>
          <icon
            class="close-icon"
            name="close"
            @click="removeRole(role, state.selectedUser)"
          />
        </span>
      </div>
      <div class="new-role-container">
        <reg-select
          name="new-role"
          :label="i18n.t('views.admin.users.new_role')"
          v-model="state.selectedRole"
          :options="selectRoleOptions"
          :disabled="selectRoleOptions.length <= 0"
        />
        <reg-button
          class="new-role-btn"
          :disabled="!state.selectedRole"
          @click="addRole(state.selectedRole, state.selectedUser)"
        >
          {{ i18n.t("views.admin.users.add_role") }}
        </reg-button>
      </div>
    </template>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive } from "vue";
import { useUsers, User } from "@/composition/user";
import { useRoles, Role } from "@/composition/role";
import DataTable from "@/components/tables/DataTable.vue";
import { useI18n } from "@/plugins/i18n";
import RegSelect from "@/components/forms/Select.vue";
import RegButton from "@/components/forms/Button.vue";
import Loading from "@/views/main/Loading.vue";
import Icon from "@/components/Icon.vue";

export default defineComponent({
  name: "UserList",
  components: { Icon, Loading, RegButton, RegSelect, DataTable },
  setup() {
    const i18n = useI18n();
    const state = reactive<UserListState>({
      loading: true,
      selectedUser: null,
      selectedRole: null,
    });
    const { state: usersState, getUsers } = useUsers();
    const {
      state: rolesState,
      getRoles,
      addRoleToUser,
      removeRoleFromUser,
    } = useRoles();
    Promise.all([getUsers(), getRoles()]).then((value) => {
      usersState.users = value[0];
      rolesState.roles = value[1];
      state.loading = false;
    });
    const updateSelectedUser = (user: User) => {
      const newUserList = [];
      for (const u of usersState.users) {
        if (u.username === user.username) {
          newUserList.push(user);
        } else {
          newUserList.push(u);
        }
      }
      usersState.users = newUserList;
      state.selectedUser = user;
    };
    const addRole = async (role: string, user: User) => {
      const filter = rolesState.roles.filter((r) => r.name === role);
      if (filter.length > 0) {
        const f_role = filter[0];
        const r_user = await addRoleToUser(f_role, user);
        updateSelectedUser(r_user);
      }
    };
    const removeRole = async (role: Role, user: User) => {
      const r_user = await removeRoleFromUser(role, user);
      updateSelectedUser(r_user);
    };
    return {
      i18n,
      state,
      usersState,
      rolesState,
      addRole,
      removeRole,
    };
  },
  computed: {
    selectRoleOptions(): { key: string; label: string; value: Role }[] {
      if (!this.state.selectedUser) return [];
      const userRoles = (this.state.selectedUser.roles || []).map(
        (r) => r.name
      );
      return this.rolesState.roles
        .filter((r) => !userRoles.includes(r.name))
        .map((r) => ({
          key: r.name,
          label: r.name,
          value: r,
        }));
    },
    tableColumns(): { key: string; name: string }[] {
      return [
        {
          key: "username",
          name: this.i18n.t("views.admin.users.columns.username"),
        },
        {
          key: "email",
          name: this.i18n.t("views.admin.users.columns.email"),
        },
        {
          key: "roles",
          name: this.i18n.t("views.admin.users.columns.roles"),
        },
      ];
    },
  },
  methods: {
    clickUserLine(user: User) {
      this.state.selectedUser = user;
    },
  },
});

interface UserListState {
  loading: boolean;
  selectedUser: User | null;
  selectedRole: string | null;
}
</script>

<style lang="scss" scoped>
@import "../../styles/variables";

.admin-users {
  .table-title {
    margin-bottom: 25px;
  }

  .user-line {
    cursor: pointer;
  }

  .user-details-title {
    margin-top: 25px;

    > span {
      margin-left: 5px;
      font-size: 75%;
      opacity: 0.75;
    }
  }

  .role-tag {
    background: $accent-dark;
    color: $accent-white;
    font-weight: bold;
    padding: 2px 8px;
    border-radius: 20px;

    &:not(:last-child) {
      margin-right: 5px;
    }

    &.with-icon {
      display: flex;
      align-items: center;

      .close-icon {
        cursor: pointer;
      }
    }
  }

  .user-roles {
    .role-tag:first-of-type {
      margin-left: 5px;
    }
  }

  .new-role-container {
    display: flex;
    align-items: flex-end;
    margin-top: 5px;

    .new-role-btn {
      margin-bottom: 3px;
      margin-left: 5px;
    }
  }
}
</style>
