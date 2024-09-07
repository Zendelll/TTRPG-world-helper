<template>
    <div>
      <h2>Create Entity</h2>
      <form @submit.prevent="createEntity">
        <label for="name">Name:</label>
        <input v-model="entity.name" type="text" id="name" required />
  
        <label for="description">Description:</label>
        <textarea v-model="entity.description" id="description"></textarea>
  
        <label for="type">Type:</label>
        <select v-model="entity.type" id="type">
          <option value="place">Place</option>
          <option value="character">Character</option>
          <option value="event">Event</option>
          <option value="folder">Folder</option>
        </select>
  
        <label for="parent_id">Parent ID (optional):</label>
        <input v-model="entity.parent_id" type="text" id="parent_id" />
  
        <button type="submit">Create Entity</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        entity: {
          name: '',
          description: '',
          type: 'place',
          parent_id: '',
        },
      };
    },
    methods: {
      async createEntity() {
        try {
          const response = await axios.post('http://localhost:8000/place', this.entity);
          console.log('Entity created', response.data);
        } catch (error) {
          console.error('Error creating entity:', error);
        }
      },
    },
  };
  </script>
  