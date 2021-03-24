<template>
  <div>see ya!</div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { useI18n } from "@/plugins/i18n";

export default defineComponent({
  name: "Home",
  setup() {
    const i18n = useI18n();
    return {
      i18n,
    };
  },
  mounted() {
    this.$router.push({
      name: "ArticleHome",
      params: { lang: this.i18n.locale.value },
    });
  },
});
</script>

<style lang="scss" scoped></style>
