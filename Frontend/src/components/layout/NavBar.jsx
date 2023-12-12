import {
  AppBar,
  Box,
  Drawer,
  Toolbar,
  Typography,
} from "@mui/material";
import MenuList from "./MenuList";

const drawerWidth = 240;

export default function NavBar() {
  
  return (
    <>
      <AppBar
        position="fixed"
        sx={{ zIndex: (theme) => theme.zIndex.drawer + 1 }}
      >
        <Toolbar>
          <Typography variant="h4" noWrap component="div">
            Seguimiento de Pozos
          </Typography>
        </Toolbar>
      </AppBar>

      <Drawer
        variant="permanent"
        sx={{
          width: drawerWidth,
          flexShrink: 0,
          [`& .MuiDrawer-paper`]: {
            width: drawerWidth,
            boxSizing: "border-box",
          },
        }}
      >
        <Toolbar />
        <Box sx={{ overflow: "auto" }}>
          <MenuList  />
        </Box>
      </Drawer>
    </>
  );
}
