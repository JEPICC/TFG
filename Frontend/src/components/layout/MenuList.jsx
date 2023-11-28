import List from "@mui/material/List";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import Collapse from "@mui/material/Collapse";
import ExpandLess from "@mui/icons-material/ExpandLess";
import ExpandMore from "@mui/icons-material/ExpandMore";
import DashboardIcon from '@mui/icons-material/Dashboard';
import RouterIcon from '@mui/icons-material/Router';
import OilBarrelIcon from '@mui/icons-material/OilBarrel';
import SendIcon from '@mui/icons-material/Send';
import { useEffect, useState } from "react";
import { NavLink } from "react-router-dom";

export default function NestedList() {
  const [wells, setWells] = useState([])

  useEffect(()=>{
    fetch("http://localhost:8000/wells")
    .then( response => response.json())
    .then( data => setWells(data))
    .catch(error => console.log(error))
  },[])


  const [open, setOpen] = useState(false);

  const handleClick = () => {
    setOpen(!open);
  };

  return (
    <List
      sx={{ width: "100%", maxWidth: 360, bgcolor: "background.paper" }}
      component="nav"
      aria-labelledby="nested-list-subheader"
    >
      <ListItemButton component={NavLink} to={"/"}>
        <ListItemIcon>
          <DashboardIcon />
        </ListItemIcon>
        <ListItemText primary="Tablero" />
      </ListItemButton>
      <ListItemButton component={NavLink} to={"/comm"}>
        <ListItemIcon>
          <RouterIcon />
        </ListItemIcon>
        <ListItemText primary="Comunicaciones" />
      </ListItemButton>
      <ListItemButton onClick={handleClick}>
        <ListItemIcon>
          <OilBarrelIcon />
        </ListItemIcon>
        <ListItemText primary="Pozos" />
        {open ? <ExpandLess /> : <ExpandMore />}
      </ListItemButton>
      <Collapse in={open} timeout="auto" unmountOnExit>
        <List component="div" disablePadding>
          {wells.sort((a,b)=> a.sigla < b.sigla ? -1 : 1)
          .map((item)=>(
          <ListItemButton component={NavLink} to="/well" 
             key={item._id}
             sx={{ pl: 4 }}
             state={{wid:item._id, sigla: item.sigla}}>
            <ListItemIcon>
              <SendIcon />
            </ListItemIcon>
            <ListItemText primary= {item.sigla} />
          </ListItemButton>
        ))}
        </List>
      </Collapse>
    </List>
  );
}
