import { RouteRecordRaw } from "vue-router";
import LanguageHome from "@/views/home/LanguageHome.vue";
import Article from "@/views/article/Article.vue";

const articleRoutes: Array<RouteRecordRaw> = [
  {
    path: "/:language",
    name: "LanguageHome",
    component: LanguageHome,
    props: (route) => ({ language: route.params.language }),
  },
  {
    path: "/:language/:id",
    name: "Article",
    component: Article,
    props: (route) => ({
      language: route.params.language,
      id: route.params.id,
    }),
  },
];

export default articleRoutes;
