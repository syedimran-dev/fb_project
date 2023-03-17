import React, { useState, useEffect } from 'react'



const Home = () => {
  const logged = localStorage.getItem("REACT_TOKEN_AUTH_KEY")
  const [message, setMessage] = useState([])

  useEffect(() => {
    fetch('/post/posts', {
      headers:{
        'content-type': 'application/json',
        'Authorization': `Bearer ${JSON.parse(logged)}`

      },
    })
      .then(response => response.json())
      .then(data => {
        console.log(data)
        setMessage(data)
      })
  }, [])

 
  return (
    <div className="container">
      {logged ? (
          message.map((post) => (
            <div key={post.id}>
              <h1>{post.title}</h1>
              <h1>{post.description}</h1>
              <h1>{post.created_on}</h1>
              <h1>{post.media}</h1>
            </div>
          ))
      ) :(<h1>Please Login First</h1>)}
    </div>
  )
}

export default Home