import java.util.ArrayList;
import java.util.List;

public class LibraryManagementSystem {
    private List<Book> books;
    private List<Member> members;

    /**
     * Constructs a new LibraryManagementSystem with empty lists for books and members.
     * 
     * Initializes two empty ArrayLists to track books and members in the library system.
     * This constructor prepares the library management system for adding books and registering members.
     */
    public LibraryManagementSystem() {
        this.books = new ArrayList<>();
        this.members = new ArrayList<>();
    }

    /**
     * Adds a new book to the library's collection.
     *
     * @param book The Book object to be added to the library's book list
     * @throws IllegalArgumentException if the book is null
     */
    public void addBook(Book book) {
        books.add(book);
    }

    /**
     * Registers a new member in the library management system.
     *
     * @param member The member to be added to the library's member list. Must not be null.
     * @throws IllegalArgumentException if the member is null or already exists in the system
     */
    public void registerMember(Member member) {
        members.add(member);
    }

    /**
     * Borrows a book for a member in the library management system.
     *
     * @param memberId The unique identifier of the member attempting to borrow the book.
     * @param bookId The unique identifier of the book to be borrowed.
     * @throws Exception if the book is not available for borrowing or the member is not registered in the system.
     *
     * @implNote This method performs the following steps:
     * 1. Finds the member by their ID using {@code findMemberById}
     * 2. Finds the book by its ID using {@code findBookById}
     * 3. Checks if the book is available
     * 4. If available, marks the book as unavailable and adds it to the member's borrowed books
     * 5. If not available, throws an exception
     */
    public void borrowBook(String memberId, String bookId) throws Exception {
        Member member = findMemberById(memberId);
        Book book = findBookById(bookId);
        if (book.isAvailable()) {
            book.setAvailable(false);
            member.borrowBook(book);
        } else {
            throw new Exception("Book is not available");
        }
    }

    /**
     * Finds a member in the library system by their unique identifier.
     *
     * @param memberId the unique ID of the member to search for
     * @return the Member object with the matching ID
     * @throws Exception if no member is found with the given ID
     */
    private Member findMemberById(String memberId) throws Exception {
        for (Member member : members) {
            if (member.getId().equals(memberId)) {
                return member;
            }
        }
        throw new Exception("Member not found");
    }

    /**
     * Finds a book in the library's collection by its unique identifier.
     *
     * @param bookId the unique identifier of the book to search for
     * @return the Book object matching the given book ID
     * @throws Exception if no book with the specified ID is found in the collection
     */
    private Book findBookById(String bookId) throws Exception {
        for (Book book : books) {
            if (book.getId().equals(bookId)) {
                return book;
            }
        }
        throw new Exception("Book not found");
    }
}

class Book {
    private String id;
    private String title;
    private boolean available;

    /**
     * Constructs a new Book instance with the specified ID and title.
     *
     * @param id A unique identifier for the book
     * @param title The title of the book
     * 
     * Initializes the book as available for borrowing by default.
     */
    public Book(String id, String title) {
        this.id = id;
        this.title = title;
        this.available = true;
    }

    /**
     * Retrieves the unique identifier for this object.
     *
     * @return the unique ID as a String
     */
    public String getId() {
        return id;
    }

    /**
     * Checks if the book is currently available for borrowing.
     *
     * @return true if the book can be borrowed, false otherwise
     */
    public boolean isAvailable() {
        return available;
    }

    /**
     * Sets the availability status of the book.
     *
     * @param available A boolean indicating whether the book is currently available for borrowing
     */
    public void setAvailable(boolean available) {
        this.available = available;
    }
}

class Member {
    private String id;
    private String name;
    private List<Book> borrowedBooks;

    /**
     * Constructs a new Member with a unique identifier and name.
     *
     * @param id   The unique identifier for the member
     * @param name The name of the member
     */
    public Member(String id, String name) {
        this.id = id;
        this.name = name;
        this.borrowedBooks = new ArrayList<>();
    }

    /**
     * Retrieves the unique identifier for this object.
     *
     * @return the unique ID as a String
     */
    public String getId() {
        return id;
    }

    /**
     * Adds a book to the member's list of borrowed books.
     *
     * @param book the Book object to be added to the member's borrowed books collection
     */
    public void borrowBook(Book book) {
        borrowedBooks.add(book);
    }
}