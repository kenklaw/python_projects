public class MessageState
{
    /**
     * The last character that has been processed, regardless
     * of whether that character can be sent to the client.
     */
    private char lastChar;
    
    /**
     * The current state of the client,
     * where the state represents the progress of a message
     * toward quit.
     */
    private CurrentState state;

   /*
    * Gets the current message state
    */
    private enum CurrentState
    {
      START_STATE,
      Q_REACHED,
      QU_REACHED,
      QUI_REACHED,
      QUIT_REACHED,
      FAIL_STATE
    };

   /*
    * Gets the current message state
    */
    public MessageState()
    {
        lastChar = '\0';
        state = CurrentState.START_STATE;
    }

   /*
    * Process each character to determine if
    * quit has been reached
    * @param in: The character to test
    * cycles though inputs until state reaches QUIT_REACHED
    * @note when in == '\n', the state will be reset.
    */
    public void processChar( char in )
    {
        if( charIsSendable( in ) && Character.isLowerCase( in ))
        {

            if( state == CurrentState.START_STATE && in == 'q'  )
            {
                state = CurrentState.Q_REACHED;
            }
            else if( state == CurrentState.Q_REACHED && in == 'u'  )
            {
                state = CurrentState.QU_REACHED;
            }
            else if( state == CurrentState.QU_REACHED && in == 'i'  )
            {
                state = CurrentState.QUI_REACHED;
            }
            else if( state == CurrentState.QUI_REACHED && in == 't'  )
            {
                state = CurrentState.QUIT_REACHED;
            }
            else
            {
                state = CurrentState.FAIL_STATE;
            }
        }
        else if( in == '\n' )
        {
            this.clear();
        }        
        else if( Character.isUpperCase( in ) )
        {
            state = CurrentState.FAIL_STATE;
        }
        
        lastChar = in;
    }

   /*
    * @returns true when quit statement reached
    */
    public boolean quitReached()
    {
        return state == CurrentState.QUIT_REACHED;
    }

   /*
    * @returns the last processed character
    */
    public char getLastChar()
    {
        return lastChar;
    }

   /*
    * Reset the message state, clearing
    * the last character and the state of the machine.
    */
    public void clear()
    {
        lastChar = '\0';
        state = CurrentState.START_STATE;
    }

   /*
    * Determine whether a character can be sent back to
    * the client.
    * @param test The character to test
    * @returns true if test is an upper or lower-case
    *          letter of the English alphabet.
    */
    public boolean charIsSendable( char test )
    {
        int charInt = (int) test;
        boolean sendable = ( charInt >= 'a' && charInt <= 'z' )
                || ( charInt >= 'A' && charInt <= 'Z' );

        return sendable;
    }
}
