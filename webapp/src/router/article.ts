import { RouteLocationNormalized, RouteRecordRaw } from "vue-router";
import ArticleHome from "@/views/article/ArticleHome.vue";
import ViewArticle from "@/views/article/ViewArticle.vue";

const articleRoutes: Array<RouteRecordRaw> = [
  {
    name: "ArticleHome",
    path: "/:lang",
    component: ArticleHome,
    props: (route: RouteLocationNormalized) => ({
      lang: route.params.lang,
    }),
  },
  {
    name: "ViewArticle",
    path: "/:lang/a/:key/:name?",
    component: ViewArticle,
    props: (route: RouteLocationNormalized) => ({
      lang: route.params.lang,
      articleKey: route.params.key,
    }),
  },
];

export default articleRoutes;
