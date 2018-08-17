export const loadUser = () => {
  return (dispatch, getState) => {
    dispatch({type: "USER_LOADING"});

    const token = getState().auth.token;

    let headers = {
      "Content-Type": "application/json",
    };

    if (token) {
      headers["Authorization"] = `Token ${token}`;
    }
    return fetch("api/v1/login/", {headers, })
      .then(res => {
        // if (res.status < 500) {
        //   return res.json().then(data => {
        //     return {status: res.status, data};
        //   })
        // } else {
        //   console.log("Server Error!");
        //   throw res;
        // }
        console.log(res)
      })
      .then(res => {
        // if (res.status === 200) {
        //   dispatch({type: 'USER_LOADED', user: res.data });
        //   return res.data;
        // } else if (res.status >= 400 && res.status < 500) {
        //   dispatch({type: "AUTHENTICATION_ERROR", data: res.data});
        //   throw res.data;
        // }
        console.log('yes almost there')
      })
  }
}