<template>
    <div>
      <h2>Entities List</h2>
      <ul>
        <li v-for="entity in entities" :key="entity.id">{{ entity.name }} ({{ entity.type }})</li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        entities: [],
      };
    },
    async created() {
      try {
        const response = await axios.get('http://localhost:8000/entities');
        this.entities = response.data;
      } catch (error) {
        console.error('Error fetching entities:', error);
      }
    },
  };
  </script>
  