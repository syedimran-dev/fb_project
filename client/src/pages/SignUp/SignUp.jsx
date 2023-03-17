import React, { useState } from 'react'
import { Link } from 'react-router-dom'
import logo from '../../assets/images/facebook.PNG'
import './signup.css'
import { useForm } from 'react-hook-form'

const SignUp = () => {
    document.title = "Facebook - Signup"
    const [show, setShow] = useState(false)
    const [serverResponse, setServerResponse] = useState('')
    const { register, reset, handleSubmit, formState: { errors } } = useForm()

    const onSubmit = (data) => {
        const body = {
            f_name: data.f_name,
            l_name: data.l_name,
            email: data.email,
            password: data.password,
            profile_pic: data.profile_pic[0].name,
            dob: data.dob
        }
        const requestOption = {
            method: "POST",
            headers: {
                'content-type': 'application/json'
            },
            body: JSON.stringify(body)
        }
        fetch('/auth/signup', requestOption)
            .then(res => res.json())
            .then(data => {
                setServerResponse(data.message)
                setShow(true)
            })
            .catch(err => console.log(err))

        reset()
    }
    return (
        <div>
            <div className="container-fluid signup-bg py-5">
                <div className="container">
                    <div className="row align-items-center py-5">
                        <div className="col-lg-6">
                            <div className="fb-logo mb-4 mb-lg-0">
                                <img src={logo} alt="facebook" title='facebook' />
                                <h5 className='ms-2 mt-4'>Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusantium debitis optio quibusdam ut veniam odit accusamus at cum! Animi, eos!</h5>
                            </div>
                        </div>
                        <div className="col-lg-6">
                            <form method='' className='card p-5 custom-signup'>
                                {show?
                                    <>
                                        <div class="alert alert-success alert-dismissible fade show" role="alert" onClose={() => setShow(false)}>
                                            <strong>{serverResponse}</strong>
                                            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                                        </div>
                                    </>
                                    :
                                    <h3>SignUp Page</h3>
                                }
                                <div className="row">
                                    <div className="col-6">
                                        <div className="mb-3">
                                            <label for="f-name" className="form-label">First Name</label>
                                            <input type="text" className="form-control" id="f-name" {...register('f_name', { required: true })} />
                                            {errors.f_name && <span style={{ color: 'red' }}>Name is required</span>}
                                        </div>
                                    </div>
                                    <div className="col-6">
                                        <div className="mb-3">
                                            <label for="l-name" className="form-label">Last Name</label>
                                            <input type="text" className="form-control" id="l-name" {...register('l_name', { required: true })} />
                                            {errors.l_name && <span style={{ color: 'red' }}>Name is required</span>}
                                        </div>
                                    </div>
                                </div>
                                <div className="mb-3">
                                    <label for="profile" className="form-label">Profile Pic</label>
                                    <input type="file" className="form-control" id="profile" {...register('profile_pic', { required: true })} />
                                    {errors.profile_pic && <span style={{ color: 'red' }}>Profile pic is required</span>}
                                </div>
                                <div className="mb-3">
                                    <label for="email" className="form-label">Email</label>
                                    <input type="email" className="form-control" id="email" {...register('email', { required: true, maxLength: 80 })} />
                                    {errors.email && <span style={{ color: 'red' }}>Email is required</span>}
                                </div>
                                <div className="mb-3">
                                    <label for="password" className="form-label">Password</label>
                                    <input type="password" className="form-control" id="password" {...register('password', { required: true, minLength: 8 })} />
                                    {errors.password && <span style={{ color: 'red' }}>password is required</span>}
                                </div>
                                <div className="mb-3">
                                    <label for="dob" className="form-label">Date of Birth</label>
                                    <input type="date" className="form-control" id="dob" {...register('dob', { required: true })} />
                                    {errors.dob && <span style={{ color: 'red' }}>Date of Birth is required</span>}
                                </div>
                                <button type="submit" onClick={handleSubmit(onSubmit)} className="btn btn-success py-3">Sign Up</button>
                                <span className='mt-3'>Already have an Account ? <Link to={'/'}>Login here</Link></span>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default SignUp