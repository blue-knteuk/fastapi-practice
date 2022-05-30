import styles from "../styles/Home.module.css";
import Link from "next/link";
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemText from '@mui/material/ListItemText';

export default function Sidebar() {
    return (
    <>
        <div className={styles.sidebar}>
        <nav aria-label="nav-list">
            <List>
            <ListItem>
                <ListItemButton>
                <ListItemText primary="ユーザー" />
                </ListItemButton>
            </ListItem>
            <ListItem>
                <ListItemButton component="a" href="#simple-list">
                <ListItemText primary="部門" />
                </ListItemButton>
            </ListItem>
            </List>
        </nav>
        </div>
    </>
    );
}