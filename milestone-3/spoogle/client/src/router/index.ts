import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import SearchView from "../views/SearchView.vue";
import ResultView from "../views/ResultView.vue";
import NotFoundView from "../views/NotFoundView.vue";
import MoreLikeThisView from "../views/MoreLikeThisView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/search",
      name: "search",
      component: SearchView,
      props: true,
    },
    {
      path: "/result/:id",
      name: "result",
      component: ResultView,
      props: true,
    },
    {
      path: "/mlt",
      name: "mlt",
      component: MoreLikeThisView,
      props: true
    },
    {
      path: "/:pathMatch(.*)*",
      name: "NotFound",
      component: NotFoundView,
    },
  ],
});

export default router;
