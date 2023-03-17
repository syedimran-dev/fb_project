import React from 'react'
import { useState } from 'react'
import { useForm } from 'react-hook-form'
import { Link, useNavigate} from 'react-router-dom'
import logo from '../../assets/images/facebook.PNG'
import '../SignUp/signup.css'
import { login } from './../Auth'
const Login = () => {
    const [message, setMessage] = useState('')
    document.title = "Facebook - Login"
    const { register, reset, handleSubmit, formState: { errors } } = useForm()
    const navigate = useNavigate()
    const submitForm = (data) => {
        console.log(data)

        const requestOption = {
            method: "POST",
            headers: {
                'content-type': 'application/json'
            },
            body: JSON.stringify(data)
        }
        fetch('/auth/login', requestOption)
            .then(res => res.json())
            .then(data => {
                if (data.access_token){
                login(data.access_token)
                window.location.href = '/home';
                }else{
                    setMessage(data.message)
                }
               


            })
            .catch(err => console.log(err))

        reset()
    }
    return (
        <div>
            <div className="container-fluid  signup-bg py-5">
                <div className="container py-5">
                    <div className="row align-items-center py-5">
                        <div className="col-lg-6">
                            <div className="fb-logo mb-4 mb-lg-0">
                                <img src={logo} alt="facebook" title='facebook' />
                                <h5 className='ms-2 mt-4'>Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusantium debitis optio quibusdam ut veniam odit accusamus at cum! Animi, eos!</h5>
                            </div>
                        </div>
                        <div className="col-lg-6">
                            <form method='' className='card p-5 custom-signup'>
                                <h3 className='mb-3 text-center'>Login Form</h3>
                                <p>{message}</p>
                                <div className="mb-3">
                                    <label for="email" className="form-label">Email</label>
                                    <input type="email" className="form-control" id="email" {...register('email', { required: true })} />
                                    {errors.email && <span style={{ color: "red" }}>Email Required</span>}
                                </div>
                                <div className="mb-3">
                                    <label for="password" className="form-label">Password</label>
                                    <input type="password" className="form-control" id="password" {...register('password', { required: true })} />
                                    {errors.password && <span style={{ color: "red" }}>Password Required</span>}
                                </div>
                                <button type="submit" onClick={handleSubmit(submitForm)} className="btn btn-success py-3">Login</button>
                                <span className='mt-3'>Doesn't have an Account ? <Link to={'/signup'}>SignUp here</Link></span>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    )
}

export default Login