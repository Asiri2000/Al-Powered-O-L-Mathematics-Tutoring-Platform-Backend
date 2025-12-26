import React, { useEffect, useState } from 'react';
import { getAllUsers, updateUserRole, deleteUser } from '../../api';
import { Trash2, Search, Shield, User, Users, ArrowLeft } from 'lucide-react';
import { useNavigate } from 'react-router-dom';

const UserDetails = () => {
  const navigate = useNavigate();
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    fetchUsers();
  }, []);

  const fetchUsers = async () => {
    try {
      const data = await getAllUsers();
      setUsers(data);
    } catch (err) {
      setError('Failed to fetch users.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleRoleChange = async (userId, newRole) => {
    const confirmed = window.confirm(`Change role to ${newRole}?`);
    if (!confirmed) return;
    
    const previousUsers = [...users];
    setUsers(users.map(user => 
      user.id === userId ? { ...user, user_role: newRole } : user
    ));

    try {
      await updateUserRole(userId, newRole);
    } catch (err) {
      alert("Failed to update role");
      setUsers(previousUsers);
    }
  };

  const handleDelete = async (userId) => {
    if (window.confirm("Are you sure you want to delete this user?")) {
      const previousUsers = [...users];
      setUsers(users.filter(user => user.id !== userId));

      try {
        await deleteUser(userId);
        alert("User deleted successfully");
      } catch (err) {
        console.error("Delete failed:", err);
        alert("Failed to delete user. They might be linked to other data.");
        setUsers(previousUsers);
      }
    }
  };

  const filteredUsers = users.filter(user => 
    user.username.toLowerCase().includes(searchTerm.toLowerCase()) ||
    (user.full_name && user.full_name.toLowerCase().includes(searchTerm.toLowerCase()))
  );

  if (loading) return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100 flex items-center justify-center">
      <div className="text-center">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-green-600 mx-auto mb-4"></div>
        <p className="text-gray-600">Loading users...</p>
      </div>
    </div>
  );

  if (error) return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100 p-8">
      <div className="max-w-6xl mx-auto">
        <div className="bg-red-50 border-2 border-red-200 rounded-xl p-6 text-center">
          <p className="text-red-700 font-semibold">{error}</p>
        </div>
      </div>
    </div>
  );

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100 p-4 sm:p-8">
      <div className="max-w-7xl mx-auto">
        
        {/* Header Section */}
        <div className="mb-8">
          <button
            onClick={() => navigate('/admin')}
            className="flex items-center gap-2 text-green-600 hover:text-green-700 font-medium mb-4 transition-colors"
          >
            <ArrowLeft className="w-4 h-4" />
            Back to Admin
          </button>
          <div className="flex items-center gap-3">
            <div className="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center">
              <Users className="w-6 h-6 text-green-600" />
            </div>
            <div>
              <h1 className="text-3xl font-bold text-slate-900">User Management</h1>
              <p className="text-slate-600">Manage all platform users and their roles</p>
            </div>
          </div>
        </div>

        {/* Stats Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
          <div className="bg-white rounded-lg shadow-sm border border-slate-200 p-4">
            <p className="text-slate-600 text-sm font-medium">Total Users</p>
            <p className="text-2xl font-bold text-slate-900 mt-1">{filteredUsers.length}</p>
          </div>
          <div className="bg-white rounded-lg shadow-sm border border-slate-200 p-4">
            <p className="text-slate-600 text-sm font-medium">Administrators</p>
            <p className="text-2xl font-bold text-purple-600 mt-1">{filteredUsers.filter(u => u.user_role === 'admin').length}</p>
          </div>
          <div className="bg-white rounded-lg shadow-sm border border-slate-200 p-4">
            <p className="text-slate-600 text-sm font-medium">Regular Users</p>
            <p className="text-2xl font-bold text-blue-600 mt-1">{filteredUsers.filter(u => u.user_role === 'user').length}</p>
          </div>
        </div>

        {/* Search Bar */}
        <div className="mb-6 relative">
          <Search className="absolute left-4 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5" />
          <input 
            type="text" 
            placeholder="Search by username or full name..." 
            className="pl-12 pr-4 py-3 border-2 border-gray-200 rounded-lg w-full focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent transition-all"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
        </div>

        {/* Users Table */}
        <div className="bg-white rounded-xl shadow-md border border-slate-200 overflow-hidden">
          <div className="overflow-x-auto">
            <table className="w-full">
              <thead>
                <tr className="bg-gradient-to-r from-slate-50 to-slate-100 border-b-2 border-slate-200">
                  <th className="px-6 py-4 text-left text-sm font-semibold text-slate-700 uppercase tracking-wide">User</th>
                  <th className="px-6 py-4 text-left text-sm font-semibold text-slate-700 uppercase tracking-wide">School / Grade</th>
                  <th className="px-6 py-4 text-left text-sm font-semibold text-slate-700 uppercase tracking-wide">Role</th>
                  <th className="px-6 py-4 text-right text-sm font-semibold text-slate-700 uppercase tracking-wide">Actions</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-200">
                {filteredUsers.length > 0 ? (
                  filteredUsers.map((user) => (
                    <tr key={user.id} className="hover:bg-slate-50 transition-colors">
                      <td className="px-6 py-4">
                        <div className="flex items-center gap-3">
                          <div className="w-10 h-10 bg-gradient-to-br from-green-100 to-green-200 rounded-full flex items-center justify-center text-green-700 font-bold">
                            {(user.full_name || user.username || "?").charAt(0).toUpperCase()}
                          </div>
                          <div>
                            <p className="font-semibold text-slate-900">{user.username}</p>
                          </div>
                        </div>
                      </td>
                      
                     

                      <td className="px-6 py-4">
                        <div className="text-sm text-slate-900 font-medium">{user.school || 'N/A'}</div>
                        {user.grade && <div className="text-xs text-slate-500">Grade {user.grade}</div>}
                      </td>

                      <td className="px-6 py-4">
                        <select
                          value={user.user_role}
                          onChange={(e) => handleRoleChange(user.id, e.target.value)}
                          className={`px-3 py-2 rounded-lg border-2 text-sm font-medium cursor-pointer transition-all ${
                            user.user_role === 'admin' 
                              ? 'border-purple-300 bg-purple-50 text-purple-700' 
                              : 'border-blue-300 bg-blue-50 text-blue-700'
                          }`}
                        >
                          <option value="user">User</option>
                          <option value="admin">Admin</option>
                        </select>
                      </td>

                      <td className="px-6 py-4 text-right">
                        <button
                          onClick={() => handleDelete(user.id)}
                          className="inline-flex items-center gap-2 px-3 py-2 text-red-600 bg-red-50 hover:bg-red-100 border border-red-200 rounded-lg transition-all hover:scale-105"
                          title="Delete user"
                        >
                          <Trash2 className="w-4 h-4" />
                          <span className="text-sm font-medium hidden sm:inline">Delete</span>
                        </button>
                      </td>
                    </tr>
                  ))
                ) : (
                  <tr>
                    <td colSpan="5" className="px-6 py-12 text-center">
                      <p className="text-gray-500 font-medium">No users found</p>
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>

          {/* Footer Info */}
          <div className="bg-slate-50 px-6 py-3 border-t border-slate-200">
            <p className="text-sm text-slate-600">
              Showing <span className="font-semibold text-slate-900">{filteredUsers.length}</span> of <span className="font-semibold text-slate-900">{users.length}</span> users
            </p>
          </div>
        </div>

      </div>
    </div>
  );
};

export default UserDetails;