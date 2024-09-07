<template>
    <div>
      <h1>Welcome to the World Helper</h1>
      <nav>
        <router-link to="/create">Create Entity</router-link> |
        <router-link to="/list">View Entities</router-link>
      </nav>
    </div>
    <div>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </div>
  </template>
  
  <script>
  export default {
    name: 'HomePage',
  };
  </script>
  