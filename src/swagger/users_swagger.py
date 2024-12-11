REGISTER_USER = {
    'tags': ['Users'],
    'summary': 'Register a new user account',
    'description': 'Create a new user account with a username, email, and password.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'description': 'The user account details',
            'schema': {
                'type': 'object',
                'properties': {
                    'username': {
                        'type': 'string',
                        'example': 'johndoe'
                    },
                    'email': {
                        'type': 'string',
                        'example': 'johndoe@example.com'
                    },
                    'password': {
                        'type': 'string',
                        'example': 'securepassword123'
                    }
                }
            }
        
        }
    ],
    'requestBody': {
        'content': {
            'application/json': {
                'example': {
                    'username': 'johndoe',
                    'email': 'johndoe@example.com',
                    'password': 'securepassword123'
                }
            }
        }
    },
    'responses': {
        200: {
            'description': 'User account created successfully',
            'content': {
                'application/json': {
                    'example': {
                        'message': 'User created successfully'
                    }
                }
            }
        },
        400: {
            'description': 'Bad request (e.g., missing or invalid fields)'
        },
        500: {
            'description': 'Internal server error'
        }
    }
}
LOGIN_USER = {
    'tags': ['Users'],
    'summary': 'User Login',
    'description': 'Login user with email and password.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'description': 'The login details',
            'schema': {
                'type': 'object',
                'properties': {
                    'email': {
                        'type': 'string',
                        'example': 'johndoe@example.com'
                    },
                    'password': {
                        'type': 'string',
                        'example': 'securepassword123'
                    }
                }
            }
        
        }
    ],
    'requestBody': {
        'content': {
            'application/json': {
                'example': {
                    'email': 'johndoe@example.com',
                    'password': 'securepassword123'
                }
            }
        }
    },
    'responses': {
        200: {
            'description': 'User account created successfully',
            'content': {
                'application/json': {
                    'example': {
                        'message': 'User created successfully'
                    }
                }
            }
        },
        400: {
            'description': 'Bad request (e.g., missing or invalid fields)'
        },
        500: {
            'description': 'Internal server error'
        }
    }
}

VERIFY_USER = {
    'tags': ['Users'],
    'summary': 'Verify a user account',
    'description': 'Verify a user account using a verification code sent to their email.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'description': 'The user account details',
            'schema': {
                'type': 'object',
                'properties': {
                    'email': {
                        'type': 'string',
                        'example': 'johndoe@example.com'
                    },
                    'verification_code': {
                        'type': 'string',
                        'example': '123456'
                    }
                }
            }
        }
    ],
    'requestBody': {
        'content': {
            'application/json': {
                'example': {
                    'email': 'johndoe@example.com',
                    'verification_code': '123456'
                }
            }
        }
    },
    'responses': {
        200: {
            'description': 'User account verified successfully',
            'content': {
                'application/json': {
                    'example': {
                        'message': 'Account verified successfully'
                    }
                }
            }
        },
        400: {
            'description': 'Invalid verification code or email'
        },
        500: {
            'description': 'Internal server error'
        }
    }
}

RESEND_VERIFICATION = {
    'tags': ['Users'],
    'summary': 'Resend the verification code',
    'description': 'Resend the verification code to the user\'s email.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'description': 'The user account details',
            'schema': {
                'type': 'object',
                'properties': {
                    'email': {
                        'type': 'string',
                        'example': 'johndoe@example.com'
                    }
                }
            }
        }
    ],
    'requestBody': {
        'content': {
            'application/json': {
                'example': {
                    'email': 'johndoe@example.com'
                }
            }
        }
    },
    'responses': {
        200: {
            'description': 'Verification code resent successfully',
            'content': {
                'application/json': {
                    'example': {
                        'message': 'Verification code resent successfully'
                    }
                }
            }
        },
        400: {
            'description': 'Email not found or invalid request'
        },
        500: {
            'description': 'Internal server error'
        }
    }
}

FORGOT_PASSWORD = {
    'tags': ['Users'],
    'summary': 'Send password reset email',
    'description': 'Send a password reset link to the user\'s email.',
    'requestBody': {
        'content': {
            'application/json': {
                'example': {
                    'email': 'johndoe@example.com'
                }
            }
        }
    },
    'responses': {
        200: {
            'description': 'Password reset email sent successfully',
            'content': {
                'application/json': {
                    'example': {
                        'message': 'Password reset email sent'
                    }
                }
            }
        },
        400: {
            'description': 'Email not found or invalid request'
        },
        500: {
            'description': 'Internal server error'
        }
    }
}

RESET_PASSWORD = {
    'tags': ['Users'],
    'summary': 'Reset the user\'s password',
    'description': 'Reset the user\'s password using the reset token and the new password.',
    'parameters': [
        {
            'name': 'token',
            'in': 'path',
            'required': True,
            'description': 'The token for resetting the user\'s password',
            'schema': {
                'type': 'string',
                'example': 'reset-token-example'
            }
        }
    ],
    'requestBody': {
        'content': {
            'application/json': {
                'example': {
                    'new_password': 'newsecurepassword123'
                }
            }
        }
    },
    'responses': {
        200: {
            'description': 'Password reset successfully',
            'content': {
                'application/json': {
                    'example': {
                        'message': 'Password reset successfully'
                    }
                }
            }
        },
        400: {
            'description': 'Invalid token or password format'
        },
        500: {
            'description': 'Internal server error'
        }
    }
}
