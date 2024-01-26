import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import javax.imageio.ImageIO;
import javax.swing.table.DefaultTableModel;


class GymManagementApp {
    private static final String DB_URL = "jdbc:mysql://localhost:3306/gym_management_system";
    private static final String DB_USER = "root";
    private static final String DB_PASSWORD = "7777";

    private static Connection connection;

    public static void main(String[] args) {
        try {
            connection = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
        } catch (Exception e) {
            e.printStackTrace();
            JOptionPane.showMessageDialog(null, "Database connection failed.");
            System.exit(0);
        }

        SwingUtilities.invokeLater(() -> createAndShowGUI());
    }

    public static void createAndShowGUI() {

        JFrame frame = new JFrame("Welcome to My Gym");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setExtendedState(JFrame.MAXIMIZED_BOTH);


        JPanel contentPanel = new JPanel();
        contentPanel.setLayout(new BoxLayout(contentPanel, BoxLayout.Y_AXIS));


        JPanel gymNamePanel = new JPanel();
        gymNamePanel.setBackground(new Color(173, 216, 230));
        JLabel gymNameLabel = new JLabel("The Fitness Centre");
        gymNameLabel.setFont(new Font("Arial", Font.BOLD, 36));
        gymNamePanel.add(gymNameLabel);
        contentPanel.add(gymNamePanel);
        JPanel gymImagesPanel = new JPanel(new FlowLayout());
        gymImagesPanel.setBackground(new Color(173, 216, 230));


        JLabel gymImageLabel1 = new JLabel();
        JLabel gymImageLabel2 = new JLabel();
        gymImagesPanel.add(gymImageLabel1);
        gymImagesPanel.add(gymImageLabel2);

        contentPanel.add(gymImagesPanel);


        JSeparator separator1 = new JSeparator();
        separator1.setForeground(Color.WHITE);
        separator1.setPreferredSize(new Dimension(1, 20));
        contentPanel.add(separator1);


        JPanel descriptionPanel = new JPanel();
        descriptionPanel.setBackground(new Color(173, 216, 230));
        JEditorPane gymDescriptionPane = new JEditorPane();
        gymDescriptionPane.setContentType("text/html");
        gymDescriptionPane.setText("<html>Your path to a healthier lifestyle. The best fitness Gym in the town<br/><br/>"
                + "<strong>Welcome to The Fitness Centre - Your Path to a Healthier You!</strong><br/><br/>"
                + "Why Choose The Fitness Centre?<br/><br/>"
                + "<ul>"
                + "<li>&#x1F3CB;&#xFE0F&zwj;&#x2642;&#FE0F; Cutting-edge equipment: Our gym boasts the latest fitness machines for effective workouts.</li>"
                + "<li>&#x1F4A1; Expert guidance: Our certified trainers are here to motivate you and help you reach your goals.</li>"
                + "<li>&#x1F3CA;&#x200D;&#x2640;&#FE0F; Varied programs: Choose from a range of workouts, from strength training to yoga and swimming.</li>"
                + "<li>&#x1F4B0; Personalized nutrition: We offer custom nutrition plans to fuel your success.</li>"
                + "<li>&#x1F41D; Supportive community: Join like-minded individuals who share your fitness passion.</li>"
                + "</ul>"
                + "</html>");
        gymDescriptionPane.setEditable(false);
        gymDescriptionPane.setPreferredSize(new Dimension(800, 350));
        gymDescriptionPane.setFont(new Font("Arial", Font.PLAIN, 18));
        descriptionPanel.add(gymDescriptionPane);
        contentPanel.add(descriptionPanel);


        JSeparator separator2 = new JSeparator();
        separator2.setForeground(Color.WHITE);
        separator2.setPreferredSize(new Dimension(1, 20));
        contentPanel.add(separator2);


        JPanel loginAndSignUpPanel = new JPanel(new FlowLayout(FlowLayout.CENTER, 20, 20));


        JPanel loginSection = new JPanel();
        loginSection.setLayout(new BoxLayout(loginSection, BoxLayout.Y_AXIS));
        loginSection.setPreferredSize(new Dimension(250, 250));

        JLabel loginLabel = new JLabel("Already a Member?");
        JButton loginButton = new JButton("Login");
        loginButton.setFont(new Font("Arial", Font.PLAIN, 18));

        loginSection.add(loginLabel);
        loginSection.add(loginButton);


        JPanel signUpSection = new JPanel();
        signUpSection.setLayout(new BoxLayout(signUpSection, BoxLayout.Y_AXIS));
        signUpSection.setPreferredSize(new Dimension(250, 250));

        JLabel signUpLabel = new JLabel("Purchase a Plan and Sign Up");
        JButton signUpButton = new JButton("Sign Up");
        signUpButton.setFont(new Font("Arial", Font.PLAIN, 18));

        signUpSection.add(signUpLabel);
        signUpSection.add(signUpButton);

        loginAndSignUpPanel.add(loginSection);
        loginAndSignUpPanel.add(signUpSection);

        contentPanel.add(loginAndSignUpPanel);
        JPanel staffAndAdminLoginPanel = new JPanel(new FlowLayout(FlowLayout.CENTER, 20, 20));


        contentPanel.add(staffAndAdminLoginPanel);
        JButton adminLoginButton = new JButton("Admin Login");
        adminLoginButton.setFont(new Font("Arial", Font.PLAIN, 18));
        staffAndAdminLoginPanel.add(adminLoginButton);


        adminLoginButton.addActionListener(e -> showAdminLoginDialog());

        JPanel buttonPanel = new JPanel();
        buttonPanel.setBackground(new Color(173, 216, 230));


        JButton viewPlansButton = new JButton("View Gym Plans");
        viewPlansButton.setFont(new Font("Arial", Font.PLAIN, 18));
        staffAndAdminLoginPanel.add(viewPlansButton);


        JSeparator separator3 = new JSeparator();
        separator3.setForeground(Color.WHITE);
        separator3.setPreferredSize(new Dimension(1, 20));
        contentPanel.add(separator3);


        JPanel contactPanel = new JPanel();
        contactPanel.setBackground(new Color(173, 216, 230));
        JTextArea contactTextArea = new JTextArea(5, 40);
        contactTextArea.setWrapStyleWord(true);
        contactTextArea.setLineWrap(true);
        contactTextArea.setOpaque(false);
        contactTextArea.setEditable(false);
        contactTextArea.setFocusable(false);
        contactTextArea.setFont(new Font("Arial", Font.PLAIN, 16));
        contactTextArea.setText("Contact us:\nEmail: info@fitnesscentre.com\nPhone: +91 7070707070\nAddress: Viman Nagar, Pune");

        contactPanel.add(contactTextArea);

        contentPanel.add(contactPanel);

      ;

        contentPanel.add(buttonPanel);

        viewPlansButton.addActionListener(e -> {
            try {

                JFrame gymPlansFrame = new JFrame("Gym Plans");
                gymPlansFrame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
                gymPlansFrame.setSize(600, 400);
                gymPlansFrame.setLocationRelativeTo(null);


                String[] columnNames = { "Plan", "Price", "Description" };
                DefaultTableModel model = new DefaultTableModel(columnNames, 0);

                try {

                    String query = "SELECT plan, price, plan_desc FROM gym_plans";
                    PreparedStatement preparedStatement = connection.prepareStatement(query);
                    ResultSet resultSet = preparedStatement.executeQuery();


                    while (resultSet.next()) {
                        String plan = resultSet.getString("plan");
                        String price = resultSet.getString("price");
                        String description = resultSet.getString("plan_desc");
                        model.addRow(new Object[]{plan, price, description});
                    }


                    JTable table = new JTable(model);
                    gymPlansFrame.add(new JScrollPane(table));

                    gymPlansFrame.setVisible(true);
                } catch (SQLException ex) {
                    ex.printStackTrace();
                    JOptionPane.showMessageDialog(null, "An error occurred while retrieving gym plans.");
                }
            } catch (Exception ex) {
                ex.printStackTrace();
                JOptionPane.showMessageDialog(null, "An error occurred while opening gym plans.");
            }
        });




        JButton staffLoginButton = new JButton("Staff Login");
        staffLoginButton.setFont(new Font("Arial", Font.PLAIN, 18));
        staffAndAdminLoginPanel.add(staffLoginButton);

        staffLoginButton.addActionListener(e -> showStaffLoginDialog());


        frame.addComponentListener(new ComponentAdapter() {
            @Override
            public void componentResized(ComponentEvent e) {
                int width = frame.getWidth() / 2;
                int height = frame.getHeight() / 2;

                if (width > 0 && height > 0) {
                    ImageIcon gymImage1 = loadImage("gym2.jpeg", width, height);
                    ImageIcon gymImage2 = loadImage("gym4.jpg", width, height);

                    gymImageLabel1.setIcon(gymImage1);
                    gymImageLabel2.setIcon(gymImage2);
                }
            }
        });

        frame.dispatchEvent(new ComponentEvent(frame, ComponentEvent.COMPONENT_RESIZED));


        loginButton.addActionListener(e -> showLoginDialog());
        signUpButton.addActionListener(e -> showSignUpDialog());


        JScrollPane scrollPane = new JScrollPane(contentPanel);
        frame.add(scrollPane);

        frame.pack();
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }

    private static ImageIcon loadImage(String filename, int width, int height) {
        try {
            BufferedImage img = ImageIO.read(new File(filename));
            Image scaledImg = img.getScaledInstance(width, height, Image.SCALE_SMOOTH);
            return new ImageIcon(scaledImg);
        } catch (IOException e) {
            e.printStackTrace();
            return new ImageIcon();
        }
    }
    private static void showAdminLoginDialog() {
        JFrame adminLoginFrame = new JFrame("Admin Login");
        adminLoginFrame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        adminLoginFrame.setSize(400, 200);
        adminLoginFrame.setLocationRelativeTo(null);

        JPanel adminLoginPanel = new JPanel(new GridLayout(3, 2, 10, 10));
        adminLoginFrame.add(adminLoginPanel);

        JTextField adminUsernameField = new JTextField(20);
        JPasswordField adminPasswordField = new JPasswordField(20);

        JButton adminLoginBtn = new JButton("Admin Login");

        adminLoginPanel.add(new JLabel("Admin Username:"));
        adminLoginPanel.add(adminUsernameField);
        adminLoginPanel.add(new JLabel("Admin Password:"));
        adminLoginPanel.add(adminPasswordField);
        adminLoginPanel.add(new JLabel()); // Empty label for spacing
        adminLoginPanel.add(adminLoginBtn);

        adminLoginBtn.addActionListener(e -> {
            String adminUsername = adminUsernameField.getText();
            String adminPassword = new String(adminPasswordField.getPassword());

            if (adminUsername.equals("Alchemist") && adminPassword.equals("07070707")) {
                // Admin login successful
                JOptionPane.showMessageDialog(null, "Admin login successful.");
                new AdminFrame(connection);


                adminLoginFrame.dispose();
            } else {
                JOptionPane.showMessageDialog(null, "Admin login failed. Please check your credentials.");
            }
        });

        adminLoginFrame.setVisible(true);
    }
    private static void showStaffLoginDialog() {
        JFrame staffLoginFrame = new JFrame("Staff Login");
        staffLoginFrame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        staffLoginFrame.setSize(400, 200);
        staffLoginFrame.setLocationRelativeTo(null);

        JPanel staffLoginPanel = new JPanel(new GridLayout(3, 2, 10, 10));
        staffLoginFrame.add(staffLoginPanel);

        JTextField staffNameField = new JTextField(20);
        JTextField staffEmailField = new JTextField(20);

        JButton staffLoginBtn = new JButton("Staff Login");

        staffLoginPanel.add(new JLabel("Staff Name:"));
        staffLoginPanel.add(staffNameField);
        staffLoginPanel.add(new JLabel("Staff Email:"));
        staffLoginPanel.add(staffEmailField);
        staffLoginPanel.add(new JLabel());
        staffLoginPanel.add(staffLoginBtn);

        staffLoginBtn.addActionListener(e -> {
            String staffName = staffNameField.getText();
            String staffEmail = staffEmailField.getText();

            try {

                String checkQuery = "SELECT * FROM staff_details WHERE staff_name = ? AND email = ?";
                PreparedStatement checkStatement = connection.prepareStatement(checkQuery);
                checkStatement.setString(1, staffName);
                checkStatement.setString(2, staffEmail);
                ResultSet resultSet = checkStatement.executeQuery();

                if (resultSet.next()) {

                    JOptionPane.showMessageDialog(null, "Staff login successful.");
                    new StaffFrame(connection,staffName);


                    staffLoginFrame.dispose();
                } else {
                    JOptionPane.showMessageDialog(null, "Staff login failed. Please check your credentials.");
                }
            } catch (SQLException ex) {
                ex.printStackTrace();
                JOptionPane.showMessageDialog(null, "An error occurred during staff login.");
            }
        });

        staffLoginFrame.setVisible(true);
    }

    private static void showLoginDialog() {
        JFrame loginFrame = new JFrame("Login");
        loginFrame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        loginFrame.setSize(400, 200);
        loginFrame.setLocationRelativeTo(null);

        JPanel loginPanel = new JPanel(new GridLayout(3, 2, 10, 10));
        loginFrame.add(loginPanel);

        JTextField usernameField = new JTextField(20);
        JPasswordField passwordField = new JPasswordField(20);

        JButton loginBtn = new JButton("Login");

        loginPanel.add(new JLabel("Username:"));
        loginPanel.add(usernameField);
        loginPanel.add(new JLabel("Password:"));
        loginPanel.add(passwordField);
        loginPanel.add(new JLabel());
        loginPanel.add(loginBtn);

        loginBtn.addActionListener(e -> {
            String username = usernameField.getText();
            String password = new String(passwordField.getPassword());

            try {
                String query = "SELECT * FROM users WHERE username = ? AND password = ?";
                PreparedStatement preparedStatement = connection.prepareStatement(query);
                preparedStatement.setString(1, username);
                preparedStatement.setString(2, password);

                ResultSet resultSet = preparedStatement.executeQuery();

                if (resultSet.next()) {

                    new UserProfile(connection, username);
                    loginFrame.dispose();
                } else {
                    JOptionPane.showMessageDialog(null, "Login failed. Please check your credentials.");
                }
            } catch (SQLException ex) {
                ex.printStackTrace();
                JOptionPane.showMessageDialog(null, "An error occurred during login.");
            }
        });

        loginFrame.setVisible(true);
    }

    private static void showSignUpDialog() {
        JFrame signUpFrame = new JFrame("Sign Up");
        signUpFrame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        signUpFrame.setSize(400, 400);
        signUpFrame.setLocationRelativeTo(null);

        JPanel signUpPanel = new JPanel(new GridLayout(14, 2, 10, 10));
        signUpFrame.add(signUpPanel);

        JTextField nameField = new JTextField(20);
        JTextField usernameField = new JTextField(20);
        JTextField emailField = new JTextField(20);
        JTextField ageField = new JTextField(5);
        JRadioButton maleRadio = new JRadioButton("Male");
        JRadioButton femaleRadio = new JRadioButton("Female");
        JComboBox<String> planComboBox = new JComboBox<>(new String[]{"Basic", "Silver", "Gold", "Platinum"});
        JPasswordField passwordField = new JPasswordField(20);

        ButtonGroup genderGroup = new ButtonGroup();
        genderGroup.add(maleRadio);
        genderGroup.add(femaleRadio);

        JButton signUpBtn = new JButton("Sign Up");

        signUpPanel.add(new JLabel("Name:"));
        signUpPanel.add(nameField);
        signUpPanel.add(new JLabel("Username:"));
        signUpPanel.add(usernameField);
        signUpPanel.add(new JLabel("Email:"));
        signUpPanel.add(emailField);
        signUpPanel.add(new JLabel("Age:"));
        signUpPanel.add(ageField);
        signUpPanel.add(new JLabel("Gender:"));
        signUpPanel.add(maleRadio);
        signUpPanel.add(new JLabel());
        signUpPanel.add(femaleRadio);
        signUpPanel.add(new JLabel("Plan:"));
        signUpPanel.add(planComboBox);
        signUpPanel.add(new JLabel("Password:"));
        signUpPanel.add(passwordField);
        signUpPanel.add(new JLabel()); // Empty label for spacing
        signUpPanel.add(signUpBtn);

        signUpBtn.addActionListener(e -> {
            String name = nameField.getText();
            String username = usernameField.getText();
            String email = emailField.getText();
            int age = Integer.parseInt(ageField.getText());
            String gender = maleRadio.isSelected() ? "Male" : "Female";
            String selectedPlan = (String) planComboBox.getSelectedItem();
            String password = new String(passwordField.getPassword());

            try {

                String checkQuery = "SELECT * FROM users WHERE username = ?";
                PreparedStatement checkStatement = connection.prepareStatement(checkQuery);
                checkStatement.setString(1, username);
                ResultSet resultSet = checkStatement.executeQuery();

                if (resultSet.next()) {
                    JOptionPane.showMessageDialog(null, "Username already exists. Please choose a different username.");
                } else {

                    String insertQuery = "INSERT INTO users (name, username, email, age, gender, plan, password) VALUES (?, ?, ?, ?, ?, ?, ?)";
                    PreparedStatement preparedStatement = connection.prepareStatement(insertQuery);
                    preparedStatement.setString(1, name);
                    preparedStatement.setString(2, username);
                    preparedStatement.setString(3, email);
                    preparedStatement.setInt(4, age);
                    preparedStatement.setString(5, gender);
                    preparedStatement.setString(6, selectedPlan);
                    preparedStatement.setString(7, password);

                    int rowsInserted = preparedStatement.executeUpdate();

                    if (rowsInserted > 0) {
                        JOptionPane.showMessageDialog(null, "Sign-up successful. You can now login.");
                        signUpFrame.dispose();
                    } else {
                        JOptionPane.showMessageDialog(null, "Sign-up failed. Please try again.");
                    }
                }
            } catch (SQLException ex) {
                ex.printStackTrace();
                JOptionPane.showMessageDialog(null, "An error occurred during sign-up.");
            }
        });

        signUpFrame.setVisible(true);
    }
}
