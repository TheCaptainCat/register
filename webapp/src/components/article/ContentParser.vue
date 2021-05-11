<script lang="ts">
import { defineComponent, h, VNode, PropType } from "vue";
import { InLink } from "@/components";
import { useArticle } from "@/composition/article";

export default defineComponent({
  name: "ContentParser",
  props: {
    content: {
      type: Array as PropType<ContentNode[]>,
      required: true,
    },
    lang: {
      type: String,
      required: true,
    },
  },
  setup() {
    return {
      Article: useArticle(),
    };
  },
  render() {
    const { nodes } = this.renderNodes(this.content);
    return h("div", {}, nodes);
  },
  methods: {
    renderNodes(
      nodes: ContentNode[]
    ): { prefix: string; nodes: Array<VNode | string>; suffix: string } {
      const tags: Array<VNode | string> = [];
      for (let i = 0; i < nodes.length; i++) {
        const node = nodes[i];
        if (node.type === "link") {
          const { nodes } = this.renderNodes(node.children);
          tags.push(
            h(
              InLink,
              {
                to:
                  node.link && node.name
                    ? {
                        name: "ViewArticle",
                        params: {
                          lang: this.lang,
                          key: node.link,
                          name: this.Article.formatName(node.name),
                        },
                      }
                    : undefined,
              },
              { default: () => nodes }
            )
          );
        } else if (node.type === "tag") {
          const { nodes } = this.renderNodes(node.children);
          tags.push(h(node.tag, {}, nodes));
        } else {
          tags.push(node.text);
        }
      }
      return {
        prefix: "",
        nodes: tags,
        suffix: "",
      };
    },
  },
});

interface TextNode {
  type: "text";
  text: string;
}

interface TagNode {
  type: "tag";
  tag: string;
  children: Array<ContentNode>;
}

interface LinkNode {
  type: "link";
  link: string | null;
  name: string | null;
  children: Array<ContentNode>;
}

type ContentNode = TextNode | TagNode | LinkNode;
</script>

<style lang="scss" scoped></style>
