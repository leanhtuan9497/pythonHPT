/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication1;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;

/**
 *
 * @author Administrator
 */
public class GuiNhan {
    ServerSocket Sserver;
    public void MoCong(int cong) throws Exception{
        Sserver = new ServerSocket(cong);
        System.out.println("Da mo cong:" + cong);
    }
    
    public String Nhan() throws Exception{
        Socket c = Sserver.accept();//lap vo han de doi Client
        System.out.println("Co thang noi den");
        //Tao luong de nhan thong tin Client gui len
        InputStreamReader is = new InputStreamReader(c.getInputStream());
        //Tao bo dem de luu du lieu nhan ve
        BufferedReader r = new BufferedReader(is);
        return r.readLine();
    }
    
    public void Gui(String tb, String ip, int cong) throws Exception{
        Socket c = new Socket(ip,cong);
        System.out.println("Da ket noi len server");
        DataOutputStream out = new DataOutputStream(c.getOutputStream());
        out.writeBytes(tb);
        out.write(10);
        out.write(13);
        out.close();
        c.close();
    }
}
