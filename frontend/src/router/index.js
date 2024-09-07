import { createRouter, createWebHistory } from 'vue-router';
import Home from '../components/HomePage.vue';
import About from '../components/EntityCreate.vue'; // Example additional page

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/about',
    name: 'About',
    component: About,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
