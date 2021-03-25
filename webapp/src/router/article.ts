import { RouteLocationNormalized, RouteRecordRaw } from "vue-router";
import ArticleHome from "@/views/article/ArticleHome.vue";
import CreateArticle from "@/views/article/CreateArticle.vue";
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
    name: "CreateArticle",
    path: "/:lang/create",
    component: CreateArticle,
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
      edit: route.query.edit === "1",
    }),
  },
];

export default articleRoutes;
