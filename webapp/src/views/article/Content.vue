<template>
  <div v-if="!state.edit">
    <button @click="state.edit = true">Edit page</button>
    <div v-if="!version">
      This article is empty
    </div>
    <section v-else>
      {{ version.content }}
    </section>
  </div>
  <div v-else class="edit-panels">
    <div class="panel">
      <label>
        Edit page
        <textarea v-model="state.content" />
      </label>
      <button @click="save">Save</button>
      <button @click="cancelEdit">Cancel</button>
    </div>
    <div class="panel">
      <pre>{{ state.content }}</pre>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive, PropType } from "vue";
import { Version } from "@/composition/page/models";

interface ArticleContentState {
  edit: boolean;
  content: string;
}

export default defineComponent({
  name: "ArticleContent",
  props: {
    version: {
      type: Object as PropType<Version>
    }
  },
  setup(props) {
    const state = reactive<ArticleContentState>({
      edit: false,
      content: (props.version && props.version.content) || ""
    });

    return {
      state
    };
  },
  methods: {
    cancelEdit() {
      this.state.edit = false;
      this.state.content =
        (this.$props.version && this.$props.version.content) || "";
    },
    save() {
      this.$emit("add-version", this.state.content);
      this.state.edit = false;
    }
  }
});
</script>

<style lang="scss" scoped>
.edit-panels {
  display: flex;

  .panel {
    width: 50%;
    border: blue solid thin;

    textarea {
      width: 95%;
      height: 300px;
    }
  }
}
</style>
