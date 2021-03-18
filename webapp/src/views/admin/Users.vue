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
    <template v-if="selectedUser !== null">
      <h1 class="user-details-title">
        {{ selectedUser.username }}
        <span>{{ selectedUser.email }}</span>
      </h1>
      <div class="user-roles flex aic">
        <h4>{{ i18n.t("views.admin.users.columns.roles") }}</h4>
        <span
          v-for="role in selectedUser.roles"
          :key="role.name"
          class="role-tag"
        >
          {{ role.name }}
        </span>
      </div>
      <div class="flex aic">
        <reg-select
          name="new-role"
          :label="i18n.t('views.admin.users.new_role')"
          v-model="selectedRole"
          :options="selectRoleOptions"
          :disabled="selectRoleOptions.length <= 0"
        />
        <reg-button
          size="sm"
          :disabled="!selectedRole"
          @click="addRoleToUser(selectedRole.value, selectedUser)"
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
import RegSelect, { RegSelectOption } from "@/components/forms/Select.vue";
import RegButton from "@/components/forms/Button.vue";
import Loading from "@/views/main/Loading.vue";

export default defineComponent({
  name: "UserList",
  components: { Loading, RegButton, RegSelect, DataTable },
  setup() {
    const i18n = useI18n();
    const state = reactive({ loading: true });
    const { state: usersState, getUsers } = useUsers();
    const { state: rolesState, getRoles, addRoleToUser } = useRoles();
    Promise.all([getUsers(), getRoles()]).then((value) => {
      usersState.users = value[0];
      rolesState.roles = value[1];
      state.loading = false;
    });
    return {
      i18n,
      state,
      usersState,
      rolesState,
      addRoleToUser,
    };
  },
  data(): UserListData {
    return {
      selectedUser: null,
      selectedRole: null,
    };
  },
  computed: {
    selectRoleOptions(): { key: string; label: string; value: Role }[] {
      if (!this.selectedUser) return [];
      const userRoles = (this.selectedUser.roles || []).map((r) => r.name);
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
      this.selectedUser = user;
    },
  },
});

interface UserListData {
  selectedUser: User | null;
  selectedRole: RegSelectOption<Role> | null;
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
  }

  .user-roles {
    .role-tag:first-of-type {
      margin-left: 5px;
    }
  }
}
</style>
