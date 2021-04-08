<template>
  <div class="reg-form reg-btn-container">
    <el-button
      class="reg-btn"
      :type="type"
      :loading="loading"
      :disabled="disabled"
      :size="size"
    >
      <slot />
      <icon class="reg-btn-icon" v-if="icon" :name="icon" :size="1" />
    </el-button>
  </div>
</template>

<script lang="ts">
import { Icon } from "@/components";
import { defineComponent, PropType } from "vue";

export default defineComponent({
  name: "RegButton",
  components: {
    Icon,
  },
  props: {
    size: {
      type: String as PropType<"medium" | "small" | "mini">,
      default: "medium",
    },
    type: {
      type: String as PropType<"primary" | "success">,
      default: "primary",
    },
    icon: String,
    light: {
      type: Boolean,
      default: false,
    },
    loading: {
      type: Boolean,
      default: false,
    },
    disabled: {
      type: Boolean,
      default: false,
    },
  },
});
</script>

<style lang="scss" scoped>
.reg-btn-container {
  display: flex;

  .reg-btn {
    margin: auto;

    .reg-btn-icon {
      margin-left: 5px;
    }
  }
}
</style>
