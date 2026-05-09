import { createRouter, createWebHistory } from 'vue-router';
import HomeView from './views/HomeView.vue';
import LandmarkDetailView from './views/LandmarkDetailView.vue';
import TravelPlanView from './views/TravelPlanView.vue';

const routes = [
  { path: '/', name: 'Home', component: HomeView },
  { path: '/landmark/:id', name: 'LandmarkDetail', component: LandmarkDetailView, props: true },
  { path: '/plan', name: 'TravelPlan', component: TravelPlanView },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
