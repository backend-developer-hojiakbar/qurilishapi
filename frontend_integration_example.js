// Example of how the frontend can integrate with the backend API

// Login function
async function loginWithToken(token) {
  try {
    const response = await fetch('http://localhost:8000/api/users/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ token }),
    });
    
    if (response.ok) {
      const data = await response.json();
      // Store tokens in localStorage
      localStorage.setItem('access_token', data.access);
      localStorage.setItem('refresh_token', data.refresh);
      return { success: true, user: data.user };
    } else {
      const errorData = await response.json();
      return { success: false, error: errorData.error || 'Login failed' };
    }
  } catch (error) {
    return { success: false, error: 'Network error' };
  }
}

// Register device function
async function registerDevice(deviceId, deviceName) {
  try {
    const accessToken = localStorage.getItem('access_token');
    const response = await fetch('http://localhost:8000/api/users/devices/register/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${accessToken}`,
      },
      body: JSON.stringify({ device_id: deviceId, name: deviceName }),
    });
    
    if (response.ok) {
      const data = await response.json();
      return { success: true, device: data };
    } else {
      const errorData = await response.json();
      return { success: false, error: errorData.error || 'Device registration failed' };
    }
  } catch (error) {
    return { success: false, error: 'Network error' };
  }
}

// Get user profile
async function getProfile() {
  try {
    const accessToken = localStorage.getItem('access_token');
    const response = await fetch('http://localhost:8000/api/users/profile/', {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${accessToken}`,
      },
    });
    
    if (response.ok) {
      const data = await response.json();
      return { success: true, profile: data };
    } else {
      return { success: false, error: 'Failed to fetch profile' };
    }
  } catch (error) {
    return { success: false, error: 'Network error' };
  }
}

// Update user profile
async function updateProfile(profileData) {
  try {
    const accessToken = localStorage.getItem('access_token');
    const response = await fetch('http://localhost:8000/api/users/profile/update/', {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${accessToken}`,
      },
      body: JSON.stringify(profileData),
    });
    
    if (response.ok) {
      const data = await response.json();
      return { success: true, profile: data };
    } else {
      const errorData = await response.json();
      return { success: false, error: errorData.error || 'Failed to update profile' };
    }
  } catch (error) {
    return { success: false, error: 'Network error' };
  }
}

// Get user devices
async function getUserDevices() {
  try {
    const accessToken = localStorage.getItem('access_token');
    const response = await fetch('http://localhost:8000/api/users/devices/', {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${accessToken}`,
      },
    });
    
    if (response.ok) {
      const data = await response.json();
      return { success: true, devices: data };
    } else {
      return { success: false, error: 'Failed to fetch devices' };
    }
  } catch (error) {
    return { success: false, error: 'Network error' };
  }
}

// Remove device
async function removeDevice(deviceId) {
  try {
    const accessToken = localStorage.getItem('access_token');
    const response = await fetch(`http://localhost:8000/api/users/devices/remove/${deviceId}/`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${accessToken}`,
      },
    });
    
    if (response.ok) {
      return { success: true, message: 'Device removed successfully' };
    } else {
      const errorData = await response.json();
      return { success: false, error: errorData.error || 'Failed to remove device' };
    }
  } catch (error) {
    return { success: false, error: 'Network error' };
  }
}

// Create a new case
async function createCase(caseData) {
  try {
    const accessToken = localStorage.getItem('access_token');
    const response = await fetch('http://localhost:8000/api/cases/create/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${accessToken}`,
      },
      body: JSON.stringify(caseData),
    });
    
    if (response.ok) {
      const data = await response.json();
      return { success: true, case: data };
    } else {
      const errorData = await response.json();
      return { success: false, error: errorData.error || 'Failed to create case' };
    }
  } catch (error) {
    return { success: false, error: 'Network error' };
  }
}

// Get all cases
async function getCases() {
  try {
    const accessToken = localStorage.getItem('access_token');
    const response = await fetch('http://localhost:8000/api/cases/', {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${accessToken}`,
      },
    });
    
    if (response.ok) {
      const data = await response.json();
      return { success: true, cases: data };
    } else {
      return { success: false, error: 'Failed to fetch cases' };
    }
  } catch (error) {
    return { success: false, error: 'Network error' };
  }
}

// Get case details
async function getCaseDetails(caseId) {
  try {
    const accessToken = localStorage.getItem('access_token');
    const response = await fetch(`http://localhost:8000/api/cases/${caseId}/`, {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${accessToken}`,
      },
    });
    
    if (response.ok) {
      const data = await response.json();
      return { success: true, case: data };
    } else {
      const errorData = await response.json();
      return { success: false, error: errorData.error || 'Failed to fetch case details' };
    }
  } catch (error) {
    return { success: false, error: 'Network error' };
  }
}

// Update case
async function updateCase(caseId, caseData) {
  try {
    const accessToken = localStorage.getItem('access_token');
    const response = await fetch(`http://localhost:8000/api/cases/${caseId}/update/`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${accessToken}`,
      },
      body: JSON.stringify(caseData),
    });
    
    if (response.ok) {
      const data = await response.json();
      return { success: true, case: data };
    } else {
      const errorData = await response.json();
      return { success: false, error: errorData.error || 'Failed to update case' };
    }
  } catch (error) {
    return { success: false, error: 'Network error' };
  }
}

// Delete case
async function deleteCase(caseId) {
  try {
    const accessToken = localStorage.getItem('access_token');
    const response = await fetch(`http://localhost:8000/api/cases/${caseId}/delete/`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${accessToken}`,
      },
    });
    
    if (response.ok) {
      return { success: true, message: 'Case deleted successfully' };
    } else {
      const errorData = await response.json();
      return { success: false, error: errorData.error || 'Failed to delete case' };
    }
  } catch (error) {
    return { success: false, error: 'Network error' };
  }
}

// Add a file to a case
async function addCaseFile(caseId, fileData) {
  try {
    const accessToken = localStorage.getItem('access_token');
    const response = await fetch(`http://localhost:8000/api/cases/${caseId}/files/add/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${accessToken}`,
      },
      body: JSON.stringify(fileData),
    });
    
    if (response.ok) {
      const data = await response.json();
      return { success: true, file: data };
    } else {
      const errorData = await response.json();
      return { success: false, error: errorData.error || 'Failed to add file' };
    }
  } catch (error) {
    return { success: false, error: 'Network error' };
  }
}

// Add a participant to a case
async function addCaseParticipant(caseId, participantData) {
  try {
    const accessToken = localStorage.getItem('access_token');
    const response = await fetch(`http://localhost:8000/api/cases/${caseId}/participants/add/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${accessToken}`,
      },
      body: JSON.stringify(participantData),
    });
    
    if (response.ok) {
      const data = await response.json();
      return { success: true, participant: data };
    } else {
      const errorData = await response.json();
      return { success: false, error: errorData.error || 'Failed to add participant' };
    }
  } catch (error) {
    return { success: false, error: 'Network error' };
  }
}

// Add a task to a case
async function addTask(caseId, taskData) {
  try {
    const accessToken = localStorage.getItem('access_token');
    const response = await fetch(`http://localhost:8000/api/cases/${caseId}/tasks/add/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${accessToken}`,
      },
      body: JSON.stringify(taskData),
    });
    
    if (response.ok) {
      const data = await response.json();
      return { success: true, task: data };
    } else {
      const errorData = await response.json();
      return { success: false, error: errorData.error || 'Failed to add task' };
    }
  } catch (error) {
    return { success: false, error: 'Network error' };
  }
}

// Update a task
async function updateTask(caseId, taskId, taskData) {
  try {
    const accessToken = localStorage.getItem('access_token');
    const response = await fetch(`http://localhost:8000/api/cases/${caseId}/tasks/${taskId}/update/`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${accessToken}`,
      },
      body: JSON.stringify(taskData),
    });
    
    if (response.ok) {
      const data = await response.json();
      return { success: true, task: data };
    } else {
      const errorData = await response.json();
      return { success: false, error: errorData.error || 'Failed to update task' };
    }
  } catch (error) {
    return { success: false, error: 'Network error' };
  }
}

// Example usage:
/*
// Login
const loginResult = await loginWithToken('AD2025');
if (loginResult.success) {
  console.log('Login successful:', loginResult.user);
  
  // Register device
  const deviceResult = await registerDevice('device-123', 'My Laptop');
  if (deviceResult.success) {
    console.log('Device registered:', deviceResult.device);
  }
  
  // Get profile
  const profileResult = await getProfile();
  if (profileResult.success) {
    console.log('Profile:', profileResult.profile);
  }
  
  // Create a case
  const caseData = {
    id: 'case-001',
    title: 'Test Case',
    case_details: 'This is a test case',
    court_stage: 'Investigation',
    client_role: 'Plaintiff',
    client_name: 'John Doe',
    tags: ['criminal', 'investigation'],
    folder: null,
    timestamp: new Date().toISOString()
  };
  
  const caseResult = await createCase(caseData);
  if (caseResult.success) {
    console.log('Case created:', caseResult.case);
  }
}
*/