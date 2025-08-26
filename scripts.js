document.addEventListener("DOMContentLoaded", function() {
    const postsContainer = document.querySelector('.cards-container');

    if (postsContainer) {
        fetch('posts.json')
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(posts => {
                postsContainer.innerHTML = ''; // Clear hardcoded posts
                posts.forEach(post => {
                    const postCard = document.createElement('article');
                    postCard.className = 'post-card';
                    postCard.innerHTML = `
                        <img src="${post.image}" alt="post image for ${post.title}">
                        <h3>${post.title}</h3>
                        <p>${post.summary}</p>
                        <a href="${post.url}">Read more</a>
                    `;
                    postsContainer.appendChild(postCard);
                });
            })
            .catch(error => {
                console.error("Error fetching posts:", error);
                postsContainer.innerHTML = "<p>Could not load posts at this time.</p>";
            });
    }
});