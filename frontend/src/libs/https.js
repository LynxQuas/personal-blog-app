const API_URL = import.meta.env.VITE_API_URL;

export const register = async (userData) => {
  const res = await fetch(`${API_URL}/users`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(userData),
  });

  return await res.json();
};

export const getBlog = async (blog_id) => {
  const res = await fetch(`${API_URL}/blogs/${blog_id}`);
  return await res.json();
};

export const getBlogs = async (query) => {
  const res = await fetch(`${API_URL}/blogs?${query}`);
  return await res.json();
};

export const getLatestBlogs = async () => {
  const res = await fetch(`${API_URL}/blogs/latest`);
  return await res.json();
};

export const updateBlog = async (blog_id, updatedData, token) => {
  const res = await fetch(`${API_URL}/blogs/${blog_id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },

    body: JSON.stringify(updatedData),
  });
  return await res.json();
};

export const deleteBlog = async (blog_id, token) => {
  const res = await fetch(`${API_URL}/blogs/${blog_id}`, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
  });
  return await res.json();
};

export const createBlog = async (blogData, token) => {
  console.log(token);
  const res = await fetch(`${API_URL}/blogs/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify(blogData),
  });

  return await res.json();
};
